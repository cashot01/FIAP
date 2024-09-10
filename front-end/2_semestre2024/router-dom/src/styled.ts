import styled from "styled-components";

export const NavMenu = styled.nav`

    width: 100%;
    min-height: 8vh;
    background-color: royalblue;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;

    a{
        color: #fff;
        text-decoration: none;
        font-size: 1.3em;
    }

    span{
        color: #fff;
        font-size: 1.5em;
    }

`

export const FooterRodape = styled.footer`

    width: 100%;
    min-height: 5vh;
    background-color: #224;
    padding: 15px;
    display: flex;
    justify-content: center;
    align-items: center;

    p{
        color: #fff;
        text-align: center;
    }

`

export const MainGeral = styled.main`

    flex-grow: 1;
    width: 100%;
    padding: 20px;

    h1{
        text-align: center;
        margin: 10px;
        color: darkblue;
    }

    div{
        border: 1px solid black;
        padding: 5px;
        margin: 10px;
    }

    button{
        display: inline-block;
        padding: 10px 20px;
        background-color: #fff;

    }

`

export const Section1 = styled.section`

    width: 50%;
    min-height: 350px;
    border: 2px solid blue;
    padding: 10px;

`