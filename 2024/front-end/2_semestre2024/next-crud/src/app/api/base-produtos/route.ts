import { promises as fs } from "fs";
import { NextResponse } from "next/server";


export async function GET() {

    // busca os dados do arquivo e guarda dentro de file
    const file = await fs.readFile(process.cwd() + '/src/data/base.json', 'utf-8')
    
    // converte o arquivo em JSON e guarda em produtos
    const produtos = JSON.parse(file)

    return NextResponse.json(produtos);
    
    
}