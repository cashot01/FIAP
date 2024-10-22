import Image from "next/image";
import carro from './../image/carro.jpg'

export default function Home() {
  return (
    <div>
      <Image src={carro} alt="Bugatti"/>
    </div>
  );
}
