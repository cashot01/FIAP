package lego;

public class ImagemProduto {
    private String url;

    public ImagemProduto() {
    }

    public ImagemProduto(String url) {
        this.url = url;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @Override
    public String toString() {
        return "ImagemProduto{" +
                "url='" + url + '\'' +
                '}';
    }
}
