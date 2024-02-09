import Image from 'next/image'
import { Inter } from 'next/font/google'
import Link from 'next/link'
import styles from '@/pages/Index.module.css'
import { useState } from 'react'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const [position, setPostion] = useState({x: 30, y: 230})

    const handlerMouseHover = () => {
      const maxX = window.innerWidth - 600;
      const maxY = window.innerHeight - 300;
      const newX = Math.floor(Math.random() * maxX)
      const newY = Math.floor(Math.random() * maxY)

      console.log("width original: " + maxX)     
      console.log("height original: " + maxY)
      console.log("width nova: " + newX)     
      console.log("height nova: " + newY)

      setPostion({x: newX, y: newY})
    }

  return (
    <main className={styles.container}>
      <div className={styles.content}>
        <h2>You are a?</h2>
        <div className={styles.buttonsGroup}>
          <Link href='/portfolio' className={styles.button}>Visitant</Link>
          <Link href='#' className={styles.fakeButtonAdmin} style={{ left: `${position.x}px`, top: `${position.y}px` }} onMouseOver={handlerMouseHover}>Admin</Link>
        </div>
      </div>
      <Link href='#' className={styles.buttonAdmin}>Admin</Link>
    </main>
  )
}
