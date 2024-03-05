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

fun mostrarMenu() {
   println("--- Menu ---")
   println("1. Afegiu un viatge")
   println("2. Consultar viatges")
   println("3. Detalls viatges")
   println("4. Registrar Clients")
   println("5. Fer reserva")
   println("6. Detalls reserva")
}

fun leerOpcio(): Int {
   print("Selecciona una opcio:")
   val opcio:Int = readLine()!!.toIntOrNull()!!

   return opcio
}

fun afegirViatge() {
   print("Introdueix la destinaco del viatge: ")
   val destinacio: String = readLine()!!
   print("Introudeix el preu del viatge: ")
   val preu: Double = readLine()?.toDoubleOrNull()?: 0.0
   println(destinacio)
   println(preu)
}

fun executarOpcio(opcio: Int) {
   when (opcio) {
      1 -> afegirViatge()
      else -> println("Opcio no valida")
   }
}

fun main() {
   mostrarMenu()
   val opcio = leerOpcio()
   println(opcio)
}
