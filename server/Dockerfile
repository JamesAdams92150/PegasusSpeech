FROM python

MAINTAINER pegasus <jamesadamspub@gmail.com>

RUN apt-get update

RUN apt-get -y install wget
RUN apt-get -y install apache2
RUN pip install SpeechRecognition
RUN pip install websockets
RUN python -m pip install --upgrade pip
RUN apt-get -y install portaudio19-dev
RUN pip install pyaudio
RUN /usr/bin/python3 -V
RUN rm /var/www/html/index.html

ADD https://raw.githubusercontent.com/JamesAdams92150/PegasusSpeech/master/front/index.html /var/www/html
ADD https://raw.githubusercontent.com/JamesAdams92150/PegasusSpeech/master/front/socket.io.js /var/www/html
ADD https://raw.githubusercontent.com/JamesAdams92150/PegasusSpeech/master/back/server.py /var/www/html
ADD https://raw.githubusercontent.com/JamesAdams92150/PegasusSpeech/master/server/bash.sh /var/www/script

#ENTRYPOINT python /var/www/html/server.py
ENTRYPOINT /var/www/script/bash.sh