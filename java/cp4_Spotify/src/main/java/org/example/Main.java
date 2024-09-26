package org.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.example.entidades.Album;
import org.example.entidades.Artista;
import org.example.entidades.Musica;
import org.example.repositorios.AlbumRepositorio;
import org.example.repositorios.ArtistaRepositorio;
import org.example.repositorios.MusicaRepositorio;

import java.util.Scanner;

public class Main {
    public static ArtistaRepositorio artistaRepositorio = new ArtistaRepositorio();
    public static AlbumRepositorio albumRepositorio = new AlbumRepositorio();
    public static MusicaRepositorio musicaRepositorio = new MusicaRepositorio();
    public static Scanner scanner = new Scanner(System.in);
    public static Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        logger.info("Sistema inciando...");
        Menu();

    }

    public static void Menu() {
        while (true) {
            System.out.println("1 - Cadastrar artista");
            System.out.println("2 - Cadastrar album");
            System.out.println("3 - Cadastrar musica");
            System.out.println("4 - Listar artistas");
            System.out.println("5 - Listar albuns");
            System.out.println("6 - Listar musicas");
            System.out.println("7 - Buscar por genero musical");
            System.out.println("8 - Bucar por ano de lançamento");
            System.out.println("9 - SAIR");
            System.out.println("Opção: ");
            int opc = scanner.nextInt();
            scanner.nextLine();
            switch (opc) {
                case 1:
                    CadastrarArtista();
                    break;
                case 2:
                    CadastrarAlbum();
                    break;
                case 3:
                    CadastrarMusica();
                    break;
                case 4:
                    ListarArtistas();
                    break;
                case 5:
                    ListarAlbuns();
                    break;
                case 6:
                    ListarMusicas();
                    break;
                case 7:
                    BuscarPorGenero();
                    break;
                case 8:
                    BuscarPorAno();
                    break;
                case 9:
                    logger.info("Sistema encerrando");
                    System.exit(0);
                default:
                    System.out.println("Opção inválida");
            }
        }
    }

    public static void CadastrarArtista() {
        var artista = new Artista();
        System.out.println("Informe o nome: ");
        artista.setNome(scanner.nextLine());

        System.out.println("Informe o gênero musical: ");
        artista.setGeneroMusical(scanner.nextLine());

        artistaRepositorio.cadastrar(artista);
        logger.info("Artista cadastrado");
    }

    public static void CadastrarAlbum() {
        var album = new Album();
        System.out.println("Informe o título: ");
        album.setTitulo(scanner.nextLine());

        System.out.println("Informe o ano de lançamento: ");
        album.setAnoDeLancamento(scanner.nextInt());
        scanner.nextLine();

        albumRepositorio.cadastrar(album);
        logger.info("Album cadastrado");
    }

    public static void CadastrarMusica() {
        var musica = new Musica();
        System.out.println("Informe o titulo:");
        musica.setTitulo(scanner.nextLine());

        System.out.println("Informe a duração: ");
        musica.setDuracao(scanner.nextInt());
        scanner.nextLine();

        musicaRepositorio.cadastrar(musica);
        logger.info("Musica cadastrada");
    }

    public static void ListarArtistas() {
        artistaRepositorio.listar().forEach(System.out::println);
    }

    public static void ListarAlbuns() {
        albumRepositorio.listar().forEach(System.out::println);
    }

    public static void ListarMusicas() {
        musicaRepositorio.listar().forEach(System.out::println);
    }

    public static void BuscarPorGenero() {
        System.out.println("Informe o gênero da busca: ");
        artistaRepositorio.buscarPorGenero(scanner.nextLine()).forEach(System.out::println);
    }

    public static void BuscarPorAno() {
        System.out.println("Informe o ano da busca: ");
        albumRepositorio.buscarPorAno(scanner.nextInt()).forEach(System.out::println);
        scanner.nextLine();
    }
}