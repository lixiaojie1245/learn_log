#dnf install -y git curl zsh
#sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
#
#
#sed -e '/^plugins=(git)/c\plugins=(\n\tgit\n)' .zshrc > .zshrc.t
#cp .zshrc.t .zshrc
#

set -v
addplugins(){
	echo $1
	sed -e  '/^plugins=(/c\plugins=(\n\t'$1 .zshrc > .zshrc.t
	cp .zshrc.t .zshrc
}

##install zsh-syntax-highlighting
#git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

#addplugins zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
addplugins  zsh-autosuggestions
