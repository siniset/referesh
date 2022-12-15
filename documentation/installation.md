## Asennussohjeet lokaalille ohjelmistolle

### Vaatimukset

Ohjelmisto vaatii toimiakseen psql:n, jossa tietokanta pyörii lokaalisti, sekä Poetryn, jonka avulla projekti asennetaan sekä jonka avulla sen toimintoja käytetään sulavasti.

### Poetryn asennusohjeet

Asenna projektin riippuvudet yms komennolla `poetry install`, jonka jälkeen voit suorittaa projektin komentoja poetry invoken kautta, esimerkiksi komennolla `poetry run invoke start`, joka laittaa sovelluksen pyörimään lokaalisti oletusarvoisesti osoitteessa 127.0.0.1:5000. 
Sovellus myös vaatii toimiakseen oikein yhteyden psql-tietokantaan, joka yhdistetään lisäämällä parametrit sovellukselle .env -tiedostoon, esimerkiksi näin käyttäjällä `postgres` ja salasanalla `testi`:
`DATABASE_URL=postgresql://postgres:testi@localhost:5432`