/* 
    TOP_DOWN
        1. Gestió de Viatges:
            - Poder afegir un nou viatge a la llista.
            - Poder obtenir informació resumida de tots els viatges.
            - Donar informació detallada d'un viatge específic.

        2. Client i Reserva:
            - Registrar un nou client i obtenir un identificador únic.
            - Permetre a un client fer una reserva per a una destinació específica.
            - Donar informació detallada d'una reserva.

        3. Interfície d'Usuari:
            - Mostrar les opcions disponibles a l'usuari.
            - Executar l'acció associada a l'opció seleccionada per l'usuari.
*/


fun mostrar_Menu() {
    println("1. Afegir viatge")
    println("2. Tenir informació dels viatges")
    println("3. Tenir informació d'un viatge en específic")
    println("4. Registrar el client")
    println("5. Fer reserva")
    println("6. Obtenir informació de reserva")
    println("7. Sortir")
}

data object Viatge {
    val id: Int
    val destinacio: String
    val dataInici: String
    val dataFi: String
}

data object Client {
    val id: Int
    val nom: String
    val email: String
}

data object Reserva {
    val id: Int
    val clientId: Int
    val viatgeId: Int
}

val viatges = mutableListOf<Viatge>(
    Viatge(id = 1, destinacio = "Tokyo", dataInici = "2023-05-01", dataFi = "2023-05-12"),
    Viatge(id = 2, destinacio = "Cancun", dataInici = "2024-03-01", dataFi = "2024-04-10")
)

val clients = mutableListOf<Client>(
    Client(id = 1, nom = "Carlos Perez", email = "carlo23@gmail.com"),
    Client(id = 2, nom = "Marta Diaz", email = "marta22@gmail.com")
)

val reserves = mutableListOf<Reserva>(
    Reserva(id = 1, ID_client = 1, ID_viatge = 1),
    Reserva(id = 2, ID_client = 2, ID_viatge = 2)
)

fun afegir_Viatge(viatge: Viatge) {
}

fun resum_Viatges(): {
}

fun detalls_Viatge(ID_viatge: Int):  {
}

fun afegir_Client(client: Client): Int {
}

fun fer_Reserva(clientId: Int, ID_viatge: Int): Int {
}

fun detalls_Reserva(ID_reserva: Int):  {
}
