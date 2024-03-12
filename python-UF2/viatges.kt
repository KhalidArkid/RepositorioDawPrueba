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
   println("7. Sortir de l'aplicacio")
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
   val viatge: Map<String, Double> = MapOf(destinacio to preu)
}

fun ConsultarViatge(viatges: MuatbleList<Map<String, Double>>){
    println("Llista de viatges:")
    viatges.forEach{ viatge ->
        viatge.forEach { (destinacio,preu) ->
            println("Destinacio: ${destinacio}, Preu: ${preu}")
        }
    }
}

fun demanarDesrtinacio(): String {
   print("Introdueix desti: ")
   val destinacio: String = readLine()!!
   return destinacio
}

fun detallsViatge(viatges: MutableList<Map<String, Double>>) {
   val destino: String = demanarDesrtinacio()
   val viatge = viatges.find {it.keys.find { it == destinacio } != null}
   if (viatge != null) {
      println("Detalls del viatge:")
      viatge.forEach { (desti, preu) ->
         println("-Destinacio: ${desti}")
         println("-Preu: ${preu}")
      }
   }  else {
      println("No hi ha cap viatge amb aquest desti")   
   }   
}

fun registrarClient(clients: MuatbleList<Pair<Int, String>>) {
   val nom: String = readLine() ?: ""
   val id: Int = readLine
}

fun executarOpcio(opcio: Int, viatges: MutableList<Map<String, Double>>) {
   when (opcio) {
      1 -> afegirViatge(viatges)
      2 -> consultarViatge(viatges)
      3 -> detallsViatge(viatges)
      4 -> registrarClient()
      7 -> println("Sortint de l'aplicacio")
      else -> println("Opcio no valida")
   }
}

fun ferReserva() {

}

fun main() {
   var viatges: MutableList<Map<String, Double>> = MutableListOf<Map<String, Double>>()
   var clients: MutableList<Map<Int, String>> = MutableListOf<Map<String, Double>>()
   do {
   mostrarMenu()
   val opcio: Int = leerOpcio()
   executarOpcio(opcio, viatges)
   } while (opcio != 7)
}