from re import search


NIJA_ROCK_URL = 'https://9jarocks.net/'


def getMovieCredit(movie_url: str) -> str:
    return f"""
This API provides access to copyrighted movie content, and using it to download or stream movies without proper authorization constitutes piracy. Piracy is illegal and can lead to serious legal consequences, including fines and legal action. Additionally, accessing or distributing copyrighted content without permission violates the intellectual property rights of creators.

This API may be blocked or restricted by internet service providers (ISPs) or government authorities. Continued use of such APIs can result in loss of access or disruption of services. Please be aware that this API may be blocked in the future.

To ensure continued access to this API, please consider supporting me . If you have any questions or need further assistance, please contact the API provider or developer.
This API was scrapted from : {search(r"https?:\/\/[^\/]+", movie_url).group()}
"""
