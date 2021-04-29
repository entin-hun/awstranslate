
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3
import csv
translate = boto3.client('translate')

outFile = open("output.csv", "w")
with open('input.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        idToTranslate=row[0]
        toTranslate=row[1]
        result = translate.translate_text(Text=toTranslate,
                                        SourceLanguageCode="en",
                                        TargetLanguageCode="pt")
        lineToOutput = idToTranslate+"|"f'{result["TranslatedText"]}'+row[2]+"\n"
        print(lineToOutput)
        outFile.write(lineToOutput)
outFile.close()
