import { NavBar } from '@/components/NavBar'
import { Html, Head, Main, NextScript } from 'next/document'
import { usePathname } from 'next/navigation'



export default function Document() {
  return (
    <Html lang="pt-br">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
