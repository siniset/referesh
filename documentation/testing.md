## Testaus

Testikattavuustavoitteemme on projektissa 85% tai korkeampi. Olemme käyttäneet testaukseen Pytestiä sekä Robot Frameworkkia, joiden avulla testaaminen sekä tulosten tarkastelu on helppoa. Testit toteuvat myös automaattisesti aina production-branchin muuttuessa. Tuotannossa olevan buildin testikattavuutta voi tarkastella CodeCovin kautta painamalla etusivun README:n yläosassa olevaa badgea.

### Testauksen käyttäohje: 

Poetryn kautta Pytestin testit voi suorittaa komennolla `invoke test`, jota varten .env-tiedostoon tulee olla nimettynä `TEST_DATABASE_URL`-muuttuja. 

--Robot test info--
