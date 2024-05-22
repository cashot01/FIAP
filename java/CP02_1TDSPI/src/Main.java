import java.util.List;

public class Main {
    public static void main(String[] args) {
        /*
        * foi criado uma classe abstrata Produto que contém os atributos nome, preco, descricao, avaliacoes e imagens
        * depois, foram criadas duas classes que herdam de Produto, ProdutoDigital e ProdutoFisico
        * ProdutoDigital tem os atributos tipoDeArquivo e tamanhoDoArquivo
        * ProdutoFisico tem os atributos peso e dimensoes
        * depois, foram criadas as classes Avaliacao, ImagemProduto e Dimensoes e colocados os atributos necessários
        * depois, foram criados objetos de ProdutoDigital e ProdutoFisico e chamado o método exibirDetalhes
         */
        var produtoDigital = new ProdutoDigital(
                "Lego Fortnite",
                100.0,
                "Jogo de construção",
                List.of(
                        new Avaliacao("Leonardo", 5, "Muito bom"),
                        new Avaliacao("Rafael",4, "Bom")
                ),
                List.of(
                        new ImagemProduto("https://images.com/lego1.jpg"),
                        new ImagemProduto("https://www.lego.com/cdn/cs/set/assets/blt42c7adf188ed2eb8/75382.png?format=webply&fit=bounds&quality=60&width=800&height=800&dpr=2")
                ),
                "exe",
                1000
        );

        var produtoFisico = new ProdutoFisico(
                "Lego TIE Interceptor",
                100.0,
                "Spark memories of classic Star Wars™ saga action with this LEGO® Star Wars Ultimate Collector Series buildable TIE Interceptor model (75382) for adults. The iconic TIE Interceptor starfighter was part of the first-ever launch of LEGO Star Wars UCS sets in the year 2000; now it’s back and redesigned for even greater authenticity. Revel in buildable details, such as its distinctive wings, cockpit interior, laser cannons and rear engine.\n" +
                        "\n" +
                        "This collectible brick-built vehicle measures over 16 in. (40 cm) long and has a display stand with an information plaque, a LEGO Star Wars 25th anniversary brick and space for the included TIE Pilot LEGO minifigure and LEGO mouse droid figure.\n" +
                        "\n" +
                        "This creative building kit is part of a collection of LEGO Star Wars sets (sold separately) that offer relaxing activities for adults. It comes with step-by-step instructions, and you can also check out the LEGO Builder app for zoom and rotate viewing tools to assist you with the complex, immersive and rewarding build.\n" +
                        "\n" +
                        "Buildable TIE Interceptor model – Your mission: to build a large-scale LEGO® Star Wars™ Ultimate Collector Series version of a TIE Interceptor, first seen in Star Wars: Return of the Jedi\n" +
                        "Collectible LEGO® Star Wars™ starfighter – Use neat building techniques to recreate the TIE Interceptor’s distinctive wing design, detailed cockpit with an opening hatch, laser cannons and more\n" +
                        "A TIE Pilot and a Mouse Droid – This unique, creative building set includes a TIE Pilot LEGO® minifigure with special arm decoration, plus a LEGO mouse droid figure\n" +
                        "Made for display – Place your TIE Interceptor on the brick-built display stand, which has an information plaque, a LEGO® Star Wars™ 25th anniversary brick and space for the TIE Pilot and mouse droid\n" +
                        "LEGO® Star Wars™ gift for adults – Treat yourself or gift this premium-quality set to another passionate Star Wars fan, advanced LEGO builder or collector of LEGO Star Wars UCS sets\n" +
                        "3D building instructions – Tackle this complex build with assistance from the LEGO® Builder app, which lets you zoom in and rotate a 3D digital version of the construction model as you build\n" +
                        "LEGO® Star Wars™ sets for adults – From a galaxy far, far away to your home, LEGO Star Wars building sets for adults are designed for people like you who enjoy relaxing, creative activities\n" +
                        "Build and display – The brick-built Star Wars™ vehicle in this 1,931-piece set measures over 12.5 in. (32 cm) high, 16 in. (40 cm) long and 13 in. (33 cm) wide",
                List.of(
                        new Avaliacao("Leonardo", 5, "Muito bom"),
                        new Avaliacao("Rafael",4, "Bom")
                ),
                List.of(
                        new ImagemProduto("https://images.com/lego1.jpg"),
                        new ImagemProduto("https://www.lego.com/cdn/cs/set/assets/blt42c7adf188ed2eb8/75382.png?format=webply&fit=bounds&quality=60&width=800&height=800&dpr=2")
                ),
                0.750,
                new Dimensoes(32,40,33)
        );

        produtoFisico.exibirDetalhes();

        produtoDigital.exibirDetalhes();
    }
}