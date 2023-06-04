
// Pin des capteurs
int VCAPTEUR = A0;

// Acquisitions par seconde
int nbParSeconde = 10;
int temps;
int nbmoy = 25;

float potCapteur;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  pinMode(VCAPTEUR, INPUT);
}

void loop() {
  potCapteur = 0.0;
  for (int i = 0; i < nbmoy; i++){
    potCapteur += analogRead(VCAPTEUR);
  }

  potCapteur = potCapteur/nbmoy;

  Serial.println(potCapteur);
  temps = 1000/nbParSeconde;
  delay(temps);

}
