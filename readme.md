docker kill unisound & docker rm unisound & docker build -t unisound "$(PWD)/Base/." & docker run -i -d --name unisound --log-opt max-size=10m -v "$(PWD)/Base/":/app -v "$(PWD)/Hotfolder/":/data unisound