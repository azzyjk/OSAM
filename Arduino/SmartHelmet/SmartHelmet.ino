#include <SoftwareSerial.h>
#define Lled 5
#define Rled 6
#define echo 12
#define trig 13

SoftwareSerial BT(8, 9); // 8번 TX, 9번 RX
unsigned long curtimemillis; // 현재 시간(밀리 초 단위)
unsigned long curtimemicros; // 현재 시간(마이크로 초 단위)
unsigned long ledtimer; // led 점등 시작 시간
unsigned long usstimer; // 초음파 센서 트리거 시간
const int interval = 3000; // 3초

void setup(){
  Serial.begin(9600);
  BT.begin(9600);
  pinMode(Lled,OUTPUT);
  pinMode(Rled,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  usstimer = micros();
}

void loop(){
curtimemillis = millis(); //현재 시간 동기화
curtimemicros = micros(); //현재 시간 동기화
char val;
  
  if(BT.available()){
    val = BT.read();
  Serial.println(val);
  //방향에 따른 LED 점등
  if(val=='l'){ //left
    digitalWrite(Lled, HIGH);
    ledtimer = millis();
    }
  else if(val=='r'){ //right
    digitalWrite(Rled, HIGH);
    ledtimer = millis();
    }
  else if(val=='s'){ //straight
    digitalWrite(Rled, HIGH);
    digitalWrite(Lled, HIGH);
    ledtimer = millis();
    }
  }
 
  if(Serial.available()){
    BT.write(Serial.read());
  }

  if(curtime-ledtimer>=interval){ // 3초 지나면 LED 소등
    digitalWrite(Lled, LOW);
    digitalWrite(Rled, LOW);
  }
//----------------초음파 센서부 (10us 펄스 폭)------------------
  
  digitalWrite(trig,HIGH);
  usstimer = micros();
  if(curtimemicros-usstimer>=10){
    digitalWrite(trig,LOW);
  }

  unsigned long distance = pulseIn(echo,HIGH)*34000/1000000/2; //음속은 340m/s이므로 시간을 곱한 후 cm단위로 환산, 왕복하는데 걸린 시간이므로 2로 나눠줌
  Serial.print(distance);
  Serial.println("CM");
}
