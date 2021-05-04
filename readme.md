A Docker wrapper for: ffmpeg-normalize
https://github.com/slhck/ffmpeg-normalize

1. Install Docker.

2. Download this repository.

3. Run the following command to build the container.

docker kill unisound & docker rm unisound & docker build -t unisound "$(PWD)/Base/." 

4. Run the container:

docker run -t -d --name unisound --log-opt max-size=10m -v "$(PWD)/Base/":/app -v "$(PWD)/Hotfolder/":/data unisound

5. The container will look for new content in Hotfolder/Input, process the files, output new files in Hotfolder/Output and delete til files in otfolder/Input.