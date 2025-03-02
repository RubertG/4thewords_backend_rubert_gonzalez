CREATE DATABASE 4thewords_prueba_rubert_gonzalez;
USE 4thewords_prueba_rubert_gonzalez;

CREATE TABLE IF NOT EXISTS legend (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    legend_date DATE NOT NULL,
    province VARCHAR(100) NOT NULL,
    canton VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL,
    image_url VARCHAR(500) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO legends (name, category, description, legend_date, province, canton, district, image_url) VALUES
('La Tulevieja', 'Fantasía', 'Espíritu de una mujer que abandonó a su hijo y fue condenada a vagar por los ríos de Costa Rica.', '1920-04-03', 'Cartago', 'Turrialba', 'Santa Cruz', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/tulevieja.jpg?alt=media&token=6480772e-1a24-4113-85a1-7732eda442e8'),
('El Cadejos', 'Misterio', 'Perro espectral que protege a los borrachos y castiga a los malvados.', '1905-10-23', 'San José', 'San José', 'Hospital', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/cadejos.jpeg?alt=media&token=878e9211-1f5f-4abd-86a2-ebbba97086f0'),
('La Llorona', 'Terror', 'Espíritu de una mujer que llora desconsoladamente por sus hijos cerca de los ríos.', '1890-05-15', 'Alajuela', 'Grecia', 'San Isidro', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/la-llorona.jpeg?alt=media&token=f9dc9956-aae7-4bc2-8ce9-a5e30c67e3e7'),
('La Carreta sin Bueyes', 'Misterio', 'Carreta fantasmal que anuncia la muerte de alguien en el pueblo.', '1885-11-07', 'Heredia', 'Heredia', 'Mercedes', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/la-carreta-sin-bueyes.jpeg?alt=media&token=9ea044f4-d6a5-4056-9330-3a293e77fc09'),
('El Padre sin Cabeza', 'Terror', 'Sacerdote condenado a vagar sin cabeza por iglesias y conventos.', '1870-09-12', 'Puntarenas', 'Esparza', 'Espíritu Santo', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/el-padre-sin-cabeza.jpeg?alt=media&token=e1360275-6c9a-4aa9-bf23-e060746d14f0'),
('La Segua', 'Terror', 'Mujer hermosa que se transforma en un espectro con cabeza de caballo para castigar a los infieles.', '1800-07-22', 'Cartago', 'Cartago', 'Oriental', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/la-segua.jpeg?alt=media&token=30e4f3e7-4dc1-4ef5-89fd-c94ad616a671'),
('El Micomalo', 'Fantasía', 'Mono gigante que aterroriza a los viajeros en la selva costarricense.', '1930-06-18', 'Limón', 'Talamanca', 'Bribri', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/El-Mico-Malo.jpg?alt=media&token=179eadd6-a031-446c-9aa9-89bcfc20933c'),
('El Sisimiqui', 'Misterio', 'Un duende travieso que vive en los bosques y engaña a los caminantes con su risa burlona.', '1882-03-15', 'San José', 'Desamparados', 'San Rafael Abajo', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/sisimiqui.jpeg?alt=media&token=b59e3e0b-df65-420c-a069-6e4b36f06292'),
('Los Duendes de Costa Rica', 'Fantasía', 'Pequeños seres mágicos que juegan bromas a las personas y esconden sus pertenencias.', '1900-05-22', 'Guanacaste', 'Liberia', 'Cañas Dulces', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/los-duendes.jpg?alt=media&token=13bad50b-7953-4d6f-b979-70bb4d7d0400'),
('El Dueño del Monte', 'Misterio', 'Un espíritu protector de los bosques que castiga a quienes dañan la naturaleza.', '1956-06-14', 'Cartago', 'Turrialba', 'Central', 'https://firebasestorage.googleapis.com/v0/b/portafolio-web-c279e.appspot.com/o/due%C3%B1o-del-monte.jpg?alt=media&token=6a8c5d00-2baf-43ac-a6fb-972df77a664e');
