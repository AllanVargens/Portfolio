import styles from '@/components/NavBar.module.css'
import { useState } from 'react'


export function NavBar() {
    
    return (
        <nav className={styles.container}>
            <h3>Portfolio</h3>
            <ul>
                <li className={styles.btn}><a href="" className={styles.btnOne}>Projects</a></li>
                <li className={styles.btn}><a href="" className={styles.btnOne}>Technologies</a></li>
                <li className={styles.btn}><a href="" className={styles.btnOne}>About me</a></li>
            </ul>
        </nav>
    )
}