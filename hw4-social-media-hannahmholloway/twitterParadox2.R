tmp <- read.csv("following_count.csv")
following_count <- tmp[,2]
barplot(following_count,main="Twitter followers and their followers count",xlab="Followers sorted by number of followers they have",ylab="Count of Followers",ylim=c(0,1000))
arrows(x0=match(c(273),following_count)+12, y0=700, x1=match(c(273), following_count)+12, y1=150, length=0.07, lwd=1.5, col='blue')
text(x=match(c(273), following_count),pos=4, y=730, labels="hollowayhannah_", col='blue')
