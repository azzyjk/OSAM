#include <TimerFreeTone.h>
#include <SoftwareSerial.h>
#define Lled 0
#define LledR 1
#define TX 2
#define RX 3
#define Rled 4
#define RledR 5
#define BLled 6
#define BRled 7

#define buzzer 9
#define echoB 10
#define trigB 11
#define echoF 12
#define trigF 13


SoftwareSerial BT(TX,RX); // 2번 TX, 3번 RX
unsigned long curtimemillis; // 현재 시간(밀리 초 단위)
unsigned long curtimemicros; // 현재 시간(마이크로 초 단위)
unsigned long ledtimer; // led 점등 시작 시간
unsigned long usstimer; // 초음파 센서 트리거 시간
unsigned long usstimerB;
const int interval = 500; // 0.5초
int sound;
int soundB;
void setup(){
    Serial.begin(9600);
    BT.begin(9600);
    pinMode(Lled,OUTPUT);
    pinMode(Rled,OUTPUT);
    pinMode(BRled,OUTPUT);
    pinMode(BLled,OUTPUT);
  
    pinMode(trigF,OUTPUT);
    pinMode(echoF,INPUT);
    pinMode(trigB,OUTPUT);
    pinMode(echoB,INPUT);
    
}

void loop(){
  curtimemillis = millis(); //현재 시간 동기화
  curtimemicros = micros(); //현재 시간 동기화
  char val;
  if(BT.available()){
    digitalWrite(Lled,LOW);
    digitalWrite(Rled,LOW);
    digitalWrite(BLled,LOW);
    digitalWrite(BRled,LOW);
    
    val = BT.read();
    Serial.println(val);
    if(val=='l'){
      digitalWrite(Lled,HIGH);
      digitalWrite(BLled,HIGH);
    }
    else if(val=='r'){
      digitalWrite(Rled,HIGH);
      digitalWrite(BRled,HIGH);
    }
    else if(val=='s'){
       digitalWrite(Lled,HIGH);
       digitalWrite(Rled,HIGH);
      digitalWrite(BLled,HIGH);
      digitalWrite(BRled,HIGH);
    }
    else{
      
    }
  }
 
  if(Serial.available()){
    BT.write(Serial.read());
  }

   digitalWrite(trigF,HIGH);
   usstimer = micros();
   if(curtimemicros-usstimer>=10){
      digitalWrite(trigF,LOW);
   }

   unsigned long distance = pulseIn(echoF,HIGH)*34000/1000000/2;
   sound = map(distance, 0, 80, 0, 10);

   Serial.println(distance);
  
   digitalWrite(trigB,HIGH);
   usstimerB = micros();
   if(curtimemicros-usstimerB>=10){
      digitalWrite(trigB,LOW);
   }
  
   unsigned long distanceB = pulseIn(echoB,HIGH)*34000/1000000/2;
   soundB = map(distanceB, 0, 80, 0, 10);

   Serial.println(distanceB);
   
   /*
   if(distance <= 80){
    TimerFreeTone(buzzer, 1517, 10, 10-sound);
   }
   if(distanceB <= 80){
    TimerFreeTone(buzzer, 1517, 10, 10-soundB);
   }
   */
}
