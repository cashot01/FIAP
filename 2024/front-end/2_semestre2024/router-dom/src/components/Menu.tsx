import { Link } from "react-router-dom";
import { NavMenu } from "../styled";


export default function Menu(){

    return(
        <NavMenu>
            <Link to={'/'}> Home</Link>
            <span> | </span>
            <Link to={'/produtos'}> Produtos</Link>
        </NavMenu>
    )
}