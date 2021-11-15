// https://www.youtube.com/c/MagnoEfren
// Control de Leds -  PySide2 / PyQt5

#define ledPWM1 5  
#define ledPWM2 6
#define led1 4
#define led2 7

int slider1 = 0;
int slider2 = 0;
int coma1, coma2; 
String datos, cadena_slider1, cadena_slider2,cadena ,dato;

void setup() {
  Serial.begin(9600);
  
  pinMode(ledPWM1, OUTPUT);
  pinMode(ledPWM2, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);     
}

void loop() {
 if(Serial.available()>5){
      dato  = Serial.readString(); 
                
      coma1 = dato.indexOf(',');      
      cadena = dato.substring(coma1+1);
      coma2 = cadena.indexOf(',');      

      cadena_slider1 = dato.substring(1, coma1);
      cadena_slider2 = cadena.substring(0,coma2);
        
      slider1 = cadena_slider1.toInt();
      slider2 = cadena_slider2.toInt();  
           
      analogWrite(ledPWM1, slider1);  //pin(PWM), valor(0-255)
      analogWrite(ledPWM2, slider2);  //pin(PWM), valor(0-255)

        //Serial.print(cadena_slider1);
       // Serial.print(cadena_slider2);
     delay(10);
 }

  if(Serial.available()<4){
      char datos  = Serial.read(); 
      
      if  (datos == 'a') {
        digitalWrite(led1,HIGH);
      }
      else if (datos == 'b') { 
        digitalWrite(led1,LOW);
      }
  
      if  (datos == 'c'){
        digitalWrite(led2,HIGH);
      }
      else if (datos == 'd') { 
        digitalWrite(led2, LOW);
       }
  delay(10);
  }
}
