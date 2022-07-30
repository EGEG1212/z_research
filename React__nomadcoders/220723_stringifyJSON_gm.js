function stringifyJSON(obj) {
    if (typeof obj === "string") return `"${obj}"`;
    if (obj === null) return "null";
    if (Array.isArray(obj)){
        let arr = [];
        obj.forEach((e) => {
            arr.push(stringifyJSON(e));
        });
        return `[${arr}]`;
    }

    if (typeof === "object") {
        let obj2 = "";

        for (let i in obj) {
            if (obj[i] === undefined ||obj[i] === function () {}){//?????
                return "{}";
            }
            obj2 += `${stringifyJSON(i)}:${stringifyJSON(obj[i])}`;
        }
        obj2 = obj2.slice(0, obj2.length - 1);
        return `{${obj2}}`;
    }
    return String(obj);
}