const protagonist = require('protagonist');
const fs = require('fs')

function readFile(file){
    fs.readFile(file, 'utf-8', (err, data) =>{
        if (err){
            console.log("Error while reading the file."+err)
            process.exit(1);
        }
        else{
            validate_data(data)
        }
    });
}

function parseData(contents){
    logs = [];
    errorCount=0;
    warningCount=0;
    contents.forEach(function (content) {
        log={};
        log["type"]=content["meta"]["classes"]["content"][0]["content"]
        log["line"]=content["attributes"]["sourceMap"]["content"][0]['content'][0]["content"][0]["attributes"]["line"]["content"]
        log["message"]=content['content']
        logs[errorCount+warningCount]=log
        if(log["type"]==="warning") {
            warningCount += 1
        }
        else if(log["type"]==="error"){
            errorCount+=1
        }
        });
    var totalCount = (warningCount+errorCount);
    console.log(JSON.stringify(logs, null, 2)+"\n"+"Errors: "+errorCount+"\n"+"Warnings: "+warningCount+"\n"+"Total: "+(totalCount)+"\n");
    if (totalCount>0){
        process.exit(1);
    }
}

function validate_data(data) {

    protagonist.validate(data).then((parseResult) => {
        if(parseResult){
            parseData(parseResult["content"])
        }
  })
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });


}

readFile('apiary.apib')
