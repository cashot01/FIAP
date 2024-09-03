import styled from "styled-components";

export const NavMenu = styled.nav`

    width: 100%;
    min-height: 8vh;
    background-color: tomato;
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
    background-color: #333;
    padding: 20px;
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
        color: darkred;
    }

`

export const MainError = styled.main`

    flex-grow: 1;
    width: 100%;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #bbb;

    h1{
        color: #f00;
        font-size: 4em;
    }

`