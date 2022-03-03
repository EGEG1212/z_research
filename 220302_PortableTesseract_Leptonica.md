영상 <https://www.youtube.com/watch?v=tly77o4RL5s&list=PLa9z1lCs1x9LzCOmfym4XEXG5VFE-Lu27&index=60> <br>
스크립트 <https://juho-lee.com/archive> <br>
#10 Run & Command Prompt] 파트 6 - 무설치 테서렉트 (Tesseract)와 렙토니카 (Leptonica)로 문자인식 (OCR) <br>
<https://github.com/iseahound/Vis2> 여기에서 down-zip  <br>
다필요한건아니고  bin/tesseract <br>
<https://github.com/tesseract-ocr/tessdata_fast> 한국어 traineddata 다운받아서 bin/tesseract/testdata_fast에 넣기 <br>
새폴더 생성 / bin 옮겨가기 <br>
4:23 새폴더 안에 복분 Tesseract Script.ahk 생성 (Vis2.ahk에서 테서렉트class부분만 뽑아서 만든것) <br>
5:00 New Script.ahk에작성 <br>
#Include Tesseract Script.ahk  <br>
Tesseract:= new Tesseract() <br>
text := Tesseract.OCR("이미지파일의경로\파일명까지", "kor", "fast") ;en과 fast가 기본값 <br>
msbox % text <br>
7:13렙토니카의 프리프로세싱  <br>
 cleanup부분 주석처리 <br>
 fileProcessedImage  Temp 저장위치 <br>
  <br>
;originally from Vis2 (Vis2.ahk): https://www.autohotkey.com/boards/viewtopic.php?f=6&t=36047
;github link: https://github.com/iseahound/Vis2
;the tesseract.exe file in this link is v4

;Preprocessing
;Script uses Leptonica (leptonica_util.exe) to preprocess the image before performing OCR. Preprocessing includes image enlargement (enlarges image size by 3.5 times for width and height) and conversion to greyscale and save the result as .tif file

;OCR
;Script then performs OCR via 'tesseract.exe' using the trained data ('eng.traineddata' or other languages)

;for up to date traineddata and other languages
;https://tesseract-ocr.github.io/tessdoc/Data-Files
;https://github.com/tesseract-ocr/tessdata_fast
;https://github.com/tesseract-ocr/tessdata_best

;to use tesseract.exe outside of ahk script, simply save the traineddata file (e.g. eng.traineddata) in the same folder as tesseract.exe and pass a command such as the below in command in prompt
;"C:\Users\....\tesseract.exe" "C:\Users\juho2\Desktop\image.jpg" "C:\Users\juho2\Desktop\output"

;example usage
;~ Tesseract:=new Tesseract()
;~ MsgBox % text := Tesseract.OCR("C:\Users\juho2\desktop\1.PNG", "", "fast") ; the last parameter sets best or fast (fast by default)
;~ MsgBox % text := Tesseract.OCR("C:\Users\juho2\desktop\test2.PNG", "kor", "") ;foreign language
;~ return

class Tesseract {

	static leptonica := A_ScriptDir "\bin\leptonica_util\leptonica_util.exe"
	static tesseract := A_ScriptDir "\bin\tesseract\tesseract.exe"
	static tessdata_best := A_ScriptDir "\bin\tesseract\tessdata_best"
	static tessdata_fast := A_ScriptDir "\bin\tesseract\tessdata_fast"

	fileProcessedImage := A_Temp "\temp.tif" ;C:\Users\<UserName>\AppData\Local\Temp
	fileConvertedText := A_Temp "\temp_text.txt"

	 __New(language:=""){
		this.language := language
	 }

	OCR(image, language:="", options:="fast"){
		this.language := language
		try {
			this.preprocess(image, this.fileProcessedImage)
		if(options="best")
			this.convert_best(this.fileProcessedImage, this.fileConvertedText)
		else
			this.convert_fast(this.fileProcessedImage, this.fileConvertedText)
		text := this.getText(this.fileConvertedText)
		} catch e {
		MsgBox, 16,, % "Exception thrown!`n`nwhat: " e.what "`nfile: " e.file
		. "`nline: " e.line "`nmessage: " e.message "`nextra: " e.extra
		}
		
		this.cleanup()
		
		return text
	 }

	cleanup(){
		FileDelete, % this.fileProcessedImage
		FileDelete, % this.fileConvertedText
	}

	convert(in:="", out:="", fast:=1) {
		in := (in) ? in : this.fileProcessedImage
		out := (out) ? out : this.fileConvertedText
		fast := (fast) ? this.tessdata_fast : this.tessdata_best

		if !(FileExist(in))
			throw Exception("Input image for conversion not found.",, in)

		if !(FileExist(this.tesseract))
		   throw Exception("Tesseract not found",, this.tesseract)

		static q := Chr(0x22)
		_cmd .= q this.tesseract q " --tessdata-dir " q fast q " " q in q " " q SubStr(out, 1, -4) q
		_cmd .= (options) ? options : " -psm 6" ;Page Segmentation Mode (--psm) affects how Tesseract splits image in lines of text and words
		_cmd .= (this.language) ? " -l " q this.language q : ""
		_cmd := ComSpec " /C " q _cmd q
		RunWait % _cmd,, Hide

		if !(FileExist(out))
		   throw Exception("Tesseract failed.",, _cmd)

		return out
	}

	convert_best(in:="", out:="") {
		return this.convert(in, out, 0)
	}

	convert_fast(in:="", out:="") {
		return this.convert(in, out, 1)
	}

	getPreprocessImage() {
		return this.fileProcessedImage
	}

	getText(in:="", lines:="") {
		in := (in) ? in : this.fileConvertedText

		if !(database := FileOpen(in, "r`n", "UTF-8"))
		   throw Exception("Text file could not be found or opened.",, in)

		if (lines == "") {
		   text := RegExReplace(database.Read(), "^\s*(.*?)\s*$", "$1")
		   text := RegExReplace(text, "(?<!\r)\n", "`r`n")
		} else {
		   while (lines > 0) {
			  data := database.ReadLine()
			  data := RegExReplace(data, "^\s*(.*?)\s*$", "$1")
			  if (data != "") {
				 text .= (text) ? ("`n" . data) : data
				 lines--
			  }
			  if (!database || database.AtEOF)
				 break
		   }
		}
		database.Close()
		return text
	}


	preprocess(in:="", out:="") {
		static ocrPreProcessing := 1
		static negateArg := 2
		static performScaleArg := 1
		static scaleFactor := 3.5

		in := (in != "") ? in : this.file
		out := (out != "") ? out : this.fileProcessedImage

		if !(FileExist(in))
		   throw Exception("Input image for preprocessing not found.",, in)

		if !(FileExist(this.leptonica))
		   throw Exception("Leptonica not found",, this.leptonica)

		static q := Chr(0x22)
		_cmd .= q this.leptonica q " " q in q " " q out q
		_cmd .= " " negateArg " 0.5 " performScaleArg " " scaleFactor " " ocrPreProcessing " 5 2.5 " ocrPreProcessing  " 2000 2000 0 0 0.0"
		_cmd := ComSpec " /C " q _cmd q
		RunWait, % _cmd,, Hide
		
		; leptonica input output negateArg dark_bg_threshold performScaleArg scaleFactor perform_unsharp_mask usm_halfwidth usm_fract perform_otsu_binarize otsu_sx otsu_sy otsu_smoothx otsu_smoothy otsu_scorefract q
		; leptonica_util.exe in.png out.png 2 0.5 1 3.5 1 5 2.5 1 2000 2000 0 0 0.0 1

		if !(FileExist(out))
		   throw Exception("Preprocessing failed.",, _cmd)

		return out
	}
	
}