import { NavBar } from "@/components/NavBar";
import styles from "@/pages/portfolio/Index.module.css"
import Image from 'next/image'

export default function PortifolioPage(){
    const imageStyle = {
        width: '35.8rem',
        height: '36.7rem'
    }
    return(
        <>
            <NavBar/>
            <header className={styles.container}>
                <div className={styles.containerInfo}>
                    <h1>Allan Vargens</h1>
                    <h2>TI / Student / Full Stack</h2>
                    <p>Developer convinced that all intellectual progress dont’t must have finish and that the knowledge is the best investment.</p>
                </div>
                <div className={styles.containerImage}>
                    <div className={styles.square1}/>
                    <div className={styles.square2}/>
                    <div className={styles.square3}/>
                    <div className={styles.imageBox}>
                    <Image src='/4c5afe7e-9469-4831-979f-8250621d055f-PhotoRoom 1.svg' layout="fill" className={styles.image} alt="Author Image"/>
                    </div>
                </div>
            </header>
        </>
    )
}