const codeList = [];
let masterString = ('abcdefghijklmnopqrstuvwxyz');
const masterList = masterString.split('');
console.log(masterList);
let entryPhrase = prompt('Enter your word or phrase to be encrypted:');
const entryList = entryPhrase.split('');
console.log(entryList);

for (x = 0; x < entryList.length; x++) {
    index = masterList.indexOf(entryList[x]);
        console.log(index);
    if (entryList[x] == ' ')
        codeList.push(entryList[x]);
    else if (index <= 12) 
            console.log(masterList[index + 13]),
            codeList.push(masterList[index + 13]);
    else if (index >= 13) 
            codeList.push(masterList[index - 13]),
            console.log(masterList[index - 13]);      
}
console.log(codeList.join(''))   