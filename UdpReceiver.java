import java.net.DatagramPacket;
import java.net.DatagramSocket;
// import java.net.InetAddress;
import java.nio.charset.StandardCharsets;

public class UdpReceiver {
    public static void main(String[] args) {
        final int UDP_PORT = 4210;

        try {
            // Crear socket y vincular al puerto 4210
            DatagramSocket socket = new DatagramSocket(UDP_PORT);
            byte[] buffer = new byte[1024];

            System.out.println("Esperando datos por UDP en el puerto " + UDP_PORT + "...\n");

            while (true) {
                try {
                    // Preparar paquete para recibir mensaje
                    DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                    socket.receive(packet); // Esperar mensaje

                    // Convertir bytes a string
                    String received = new String(packet.getData(), 0, packet.getLength(), StandardCharsets.UTF_8).trim();

                    // Separar valores por coma
                    String[] valores = received.split(",");

                    // Convertir a porcentaje y mostrar
                    float x_porc = Float.parseFloat(valores[0]) * 100;
                    float y_porc = Float.parseFloat(valores[1]) * 100;

                    System.out.printf("x_porc = %.2f %% , y_porc = %.2f %%\n", x_porc, y_porc);
                } catch (Exception e) {
                    System.out.println("Algo salió mal :( ");
                }
            }

        } catch (Exception e) {
            System.err.println("No se pudo abrir el socket: " + e.getMessage());
        }
    }
}

