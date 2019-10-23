#include <SoftwareSerial.h>

SoftwareSerial BT(8, 9); // 8번 TX, 9번 RX HC-06 모듈 테스트 코드

void setup(){
  Serial.begin(9600);
  BT.begin(9600);
}

void loop(){
  if(BT.available()){ //블루투스 -> 시리얼 모니터
    Serial.write(BT.read());
  }
  if(Serial.available()){ // 시리얼 모니터 -> 블루투스
    BT.write(Serial.read());
  }
}
