# AWS Translate docker image

This image is suposed to run a Python script that uses boto3 and do something in AWS. This specific task consists in to a script (translate.py)  that uses the AWS translate service to read a input.csv file with id and description fields separated by ',', translate it  and write the results on output.csv file using the same format as the input.
XLS can be entered too but the columns is hardcoded (as languages). Feel free to change the script as you wish

## Directories
aws/ -> credentials and config
work/ -> location for the script, input file and output file

## Running
To do it, you must build the Docker image (whenever you change the Dockerfile) and run the container with:
```bash
docker build -t boto .  #Building the image
docker run -it --rm --name boto3 -v c:/users/andretapxure/desktop/awstranslate/work:/usr/src/work -v c:/users/andretapxure/desktop/awstranslate/aws:/root/.aws -w /usr/src/work boto python3 translate.py #Running the translate script
```

## Sample Data for CSV
```CSV
id,description
1,"Strain intrns musc/fasc/tend r lit fngr at wrs/hnd lv, subs"
2,Complete traumatic amputation at right shoulder joint
```