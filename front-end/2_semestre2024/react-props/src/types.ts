export type Comp1Props = {
    children: React.ReactNode;
}

export type Comp2Props = {
    autor:string;
}

export type CabecProps ={
    titulo:string;
    codigo:number;
    info: ()=> void;
}

export type AlunoProps= {
    nome:string;
    idade:number;
    index:number;
}