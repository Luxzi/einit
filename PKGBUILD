# Maintainer: Luxzi <luxzi pm me>
pkgname=einit
pkgver=1.7
pkgrel=0
epoch=1
pkgdesc='Initialize your projects with one command. Easy, Customizable, Flexable, Fast.'
arch=('any')
url="https://github.com/Luxzi/einit"
license=('GPL3')
depends=('python3' 'python-pip' 'curl')
md5sums=('SKIP')

source=("${pkgname}"::'https://github/Luxzi/einit.git')

pkgver() {
  cd "$srcdir/${pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    install ${srcdir}/${pkgname}/einit.py ${pkgdir}/usr/local/bin/${pkgname}/einit.py
    install ${srcdir}/${pkgname}/einit_globals.py ${pkgdir}/usr/local/bin/${pkgname}/einit_globals.py
    install ${srcdir}/${pkgname}/config.yaml ${pkgdir}/etc/${pkgname}/config.yaml
    mkdir /etc/${pkgname}/plugins
    install ${srcdir}/${pkgname}/README.md ${pkgdir}/usr/share/doc/${pkgname}/README
    echo "alias einit='python3 /usr/local/bin/${pkgname}/einit.py'" >> ~/.bashrc
    pip install pyyaml
    echo "INFO: Make sure to reload your terminal(s) to update their aliases to finish the install."
}