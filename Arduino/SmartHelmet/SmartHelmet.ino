#include <SoftwareSerial.h>
#define Lled 5
#define Rled 6

SoftwareSerial BT(8, 9); // 8번 TX, 9번 RX
unsigned long curtime;
unsigned long pretime;
const int interval = 3000;

void setup(){
  Serial.begin(9600);
  BT.begin(9600);
  pinMode(4,OUTPUT);
  digitalWrite(4,LOW);
}

void loop(){
curtime = millis();
char a;
  
  if(BT.available()){
    a = BT.read();
    Serial.println(a);
    if(a=='a'){
      digitalWrite(4, HIGH);
      pretime = millis();
    }
  }
  
  if(Serial.available()){
    BT.write(Serial.read());
  }

  if(curtime-pretime>=interval){ // 3초 지나면 끔
    digitalWrite(4, LOW); 
  }
}
