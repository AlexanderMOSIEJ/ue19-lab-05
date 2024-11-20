import requests

def cinq_first_crypto_marche():
    """
    Cette fonction récupère les données des 5 premières cryptomonnaies du marché
    à partir de l'API CoinLore.

    :param: Aucun paramètre d'entrée
    :return: Liste des 5 premières cryptomonnaies avec leur nom,
             symbole et prix en USD
    :rtype: list
    """

    url = "https://api.coinlore.net/api/tickers/"
    try:
        # Envoi de la requête GET à l'API
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a échoué
        data = response.json()  # Analyse la réponse JSON

        if "data" in data:
            top_5 = data["data"][:5]
            resultats = []

            for pos, coin in enumerate(top_5, start=1):
                name = coin.get("name", "Pas de nom")
                symbol = coin.get("symbol", "Aucun symbole")
                price_usd = coin.get("price_usd", "Aucun prix disponible")


                resultats.append(f"{pos:}) {name:<14} ({symbol:<4}) : {price_usd:>8} $")

            return resultats
        else:
            return ["No data found in the API response."]

    except requests.exceptions.RequestException as error:
        return [f"An error occurred: {error}"]


if __name__ == "__main__":
    crypto = cinq_first_crypto_marche()

    for i in crypto:
        print(i)

