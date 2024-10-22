import Image from 'next/image';
import carro from './../image/carro.jpg'

export default function Home() {
  return (
    <div>
      <Image src={carro} alt="Bugatti"/>
      <Image src="/image/carro.jpg" alt="Bugatti 2" width={1024} height={577}/>
      <img src="/image/carro.jpg" alt="Bugatti 3" />
      <Image src='https://assegurou.com.br/blog/wp-content/uploads/2024/03/Bugatti-La-Voiture-Noire-1024x577.jpg' alt="Bugatti 4" width={1024} height={577}/>
    </div>
  );
}
