import { NavBar } from '@/components/NavBar'
import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import { usePathname } from 'next/navigation'



export default function App({ Component, pageProps }: AppProps) {
  const navigation = usePathname()
  const excludeNavBarPages = ['/']
  return (<>
    {!excludeNavBarPages.includes(navigation) && <NavBar />}
    <Component {...pageProps} />
  </>
  )
}
