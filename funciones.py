def gradient_descent(x, y, theta_0,alpha,cost_derivate,treshold=0.001,max_iters=10000):
	theta, last_cost, i = theta_0
	while i < max_iters and abs(cost(x,y,theta) - last_cost) > treshold:
		last_cost = cost(x,y,theta)
		theta -= alpha * cost_derivate(x,y,theta)
		i++

def linear_cost(theta,X,y):
	m, n = X.shape
	h = np.matmul(X, theta)
	sq = (y - h) ** 2
	return sq.sum() / (2*m)


def derivate_cost(theta, X, y):
	h = np.matmul(X, theta)
	dif = (y-h)
	derivadaJO = (x/m)*dif.sum()
	return theta-alpha*(derJO)