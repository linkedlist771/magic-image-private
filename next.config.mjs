/** @type {import('next').NextConfig} */
const nextConfig = {
  // Uncomment the following lines for static export
  // output: 'export',
  // trailingSlash: true,
  // images: {
  //   unoptimized: true
  // },
  
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '*',
        port: '',
        pathname: '**',
      },
      {
        protocol: 'http',
        hostname: '*',
        port: '',
        pathname: '**',
      }
    ],
  }
}

export default nextConfig 