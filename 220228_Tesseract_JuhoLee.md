What is Tesseract?
Tesseract is a free optical character recognition engine originally developed by HP which was later made open source and the development is now sponsored by Google
👍
<https://www.youtube.com/watch?v=AJkqqZukJuI&t=874s>
CMD에서 설치위치로 갑니다. C:\Program Files\Tesseract-OCR <br>
**tesseract "이미지경로\파일명까지" "저장경로\output" -l kor** <br>
C:\Users\User\Desktop\ahk\CaptureKOR.png <br>
C:\Users\User\Desktop\ahk\CaptureENG.png <br>
C:\Users\User\Desktop\ahk\output <br>
tesseract "C:\Users\User\Desktop\ahk\CaptureKOR.png" "C:\Users\User\Desktop\ahk\output" -l kor <br>
😍-l kor 한글인식괜춘 (특수기호불가. 영어불가. 숫자가능. )
넉->녁 / 굶->x

--------------------------- Installation ---------------------------
Go to <https://github.com/UB-Mannheim/tesseract/wiki> (works as of April 2021)

Download "tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe (64 bit)" or any other newer version

Install Tesseract (also install any other language you need during the installation process)

------------ Install additional language and script models ---------

When you want to install additional language and script models there are two options.
A) Either you can start the installation again and choose the additional language and script models to install.
B) Or, you can install them manually (see below)

Choose the additional language and script models from e.g. one of the places linked from <https://tesseract-ocr.github.io/tessdoc/Data-Files>

Download the traineddata file to the tessdata folder of tesseract on your PC, e.g. C:\Program Files\Tesseract-OCR\tessdata. It is also possible to create new subfolders within that folder to distinguish for example the best and fast models.

Check that the new languages are recognized by

source:<https://github.com/UB-Mannheim/tesseract/wiki/Install-additional-language-and-script-models>


--------------------------- How to Use Tesseract ---------------------------

;User Manual available here: <https://tesseract-ocr.github.io/>

Run Tesseract in Cmd
;example: <https://www.lipsum.com/>

;Syntax for English:
tesseract InputFilename.ext outputName
;Note: you do not need to specify the output extension. It's going to be txt.

;if you are in Tesseract folder (ran this in cmd -> chdir "C:\Program Files\Tesseract-OCR\"):
tesseract myScreenshot.png myOutputTextFile

;if you are not in Tesseract folder in cmd:
"C:\Program Files\Tesseract-OCR\tesseract.exe" C:\Users\juho2\Desktop\Capture.PNG C:\Users\juho2\Desktop\output

;you can also wrap the parameters in quotation marks but that's not a must
"C:\Program Files\Tesseract-OCR\tesseract.exe" "C:\Users\juho2\Desktop\Capture.PNG" "C:\Users\juho2\Desktop\output"

;however you must wrap the parameters in quotation marks if your parameter includes spaces
"C:\Program Files\Tesseract-OCR\tesseract.exe" "C:\Users\juho2\Desktop\New Folder\Capture.PNG" "C:\Users\juho2\Desktop\New Folder\output"

;Syntax for Non-English:
tesseract InputFilename.ext outputName -l For
;Note: 'For' is where the three letter representing the foreign languages goes to. E.g. kor for Korean.

e.g.
"C:\Program Files\Tesseract-OCR\tesseract.exe" "C:\Users\juho2\Desktop\Capture.PNG" "C:\Users\juho2\Desktop\output" -l kor


;Page Segmentation Mode (PSM)
PSM affects how Tesseract splits image in lines of text and words.

If you're not getting the expected result, change the psm from the default of 3. Usually 6 works best.
test out with the help file text for psm (tesseract --help-psm)
tesseract.exe "C:\Users\juho2\desktop\Capture.PNG" "C:\Users\juho2\desktop\output" --psm 6

However, 6 is not always the best mode to go with. This try example https://www.lipsum.com/

to see how to use other options visit: http://manpages.ubuntu.com/manpages/cosmic/man1/tesseract.1.html

--------------------------- How to Use Tesseract via AutoHotkey ---------------------------

Use Run command

;standard
run, C:\Program Files\Tesseract-OCR\tesseract.exe "C:\Users\juho2\Desktop\Temporary Scripts\Capture.PNG" "C:\Users\juho2\Desktop\Temporary Scripts\output" --psm 6

;foreign language
Run, "C:\Program Files\Tesseract-OCR\tesseract.exe" "C:\Users\juho2\Desktop\Temporary Scripts\Capture.PNG" "C:\Users\juho2\Desktop\Temporary Scripts\output" -l kor

;Also can do it via cmd and use variables
run, cmd.exe /c "C:\Program Files\Tesseract-OCR\tesseract.exe" %A_Desktop%\Capture.PNG %A_Desktop%\output

; if test.png is saved in the same directory as the script
run, cmd.exe /c "C:\Program Files\Tesseract-OCR\tesseract.exe" Capture.PNG output

;if you must specify the paths to everything in cmd and also add psm mode
myCommandLine = ""C:\Program Files\Tesseract-OCR\tesseract.exe" "C:\Users\juho2\Desktop\Temporary Scripts\Capture.PNG" "C:\Users\juho2\Desktop\Temporary Scripts\output" --psm 6"
run, cmd.exe /c %myCommandLine%

;if you get nothing back then do /k instead of /c to see the error message

;then use the FileRead command to read the result
;note: best use the runwait command when performing the OCR
FileRead, myOCRresult, C:\Users\juho2\Desktop\Temporary Scripts\output.txt
msgbox % myOCRresult