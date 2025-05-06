from   colorama                import Fore, Back, Style, init           # type: ignore
import time

def startLabel(msg: str = 'START OF CELL OUTPUT') -> float:
    dotlength = 100 - len(msg)
    print(Fore.RED  + 100 * '-' + Fore.RESET)
    print(Fore.RED  + dotlength * '-' + msg + Fore.RESET)
    print(Fore.RED  + 100 * '-' + Fore.RESET)
    return time.time()

def endLabel(start_time):
    print(Fore.CYAN + "-------------------------------------------------Elapsed Time --- %2.20f seconds ---" % (time.time() - start_time))
    print(Fore.RED  + 100 * '-' + Fore.RESET)
    print(Fore.RED  +  82 * '-' + 'End of cell output' + Fore.RESET) 
    print(Fore.RED  + 100 * '-' + Fore.RESET)
    return None

all_time               = time.time()
start_time             = startLabel('(1) Importing Libraries')
import numpy                   as     np                                # type: ignore
import pandas                  as     pd                                # type: ignore
import matplotlib.pyplot       as     plt                               # type: ignore
from   sklearn.model_selection import train_test_split                  # type: ignore
from   statsmodels.formula.api import ols                               # type: ignore
from   sklearn.tree            import DecisionTreeRegressor             # type: ignore
from   sklearn.tree            import DecisionTreeClassifier, plot_tree # type: ignore
endLabel(start_time)
#%matplotlib inline

start_time             = startLabel('(2) Importing Data')
df                     = pd.read_csv('Amusment_Park_Attendance.csv')
endLabel(start_time)

start_time             = startLabel('(3) Data Exploration')
df.info()
endLabel(start_time)

start_time             = startLabel('(4) Data Cleaning - Categorical Variables')
categoricals           = ['month', 'day', 'hour', 'day_of_week', 'holiday']
df[categoricals]       = df[categoricals].astype('category')
endLabel(start_time)

start_time             = startLabel('(5) Data Exploration')
df.info(verbose=True)
print(Fore.RED + 100 * '-' + Fore.RESET)
print(df.items)
print(Fore.RED + 100 * '-' + Fore.RESET)
print('Index           : ',df.index)
print(Fore.RED + 100 * '-' + Fore.RESET)
print(df.describe())
print(Fore.RED + 100 * '-' + Fore.RESET)
print('Rows and Columns: ',df.shape)
print(Fore.RED + 100 * '-' + Fore.RESET)
print('Column Names    : ',df.columns)
endLabel(start_time)

start_time             = startLabel('(6) Data Exploration - Histogram')
df.hist(figsize        = (25, 25), bins=50, grid=True, layout=(4, 2), xlabelsize=10, xrot=60)
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')   
endLabel(start_time)

start_time             = startLabel('(7) Data Exploration - Sample Data - Head')
print(df.head(10))
endLabel(start_time)

start_time             = startLabel('(8) Data Splitting - Train and Test')
df_train, df_test      = train_test_split(df, test_size=0.3, shuffle=True, random_state=42)
print('Train data:',len(df_train))
print('Test data :',len(df_test))
print('Total data:',len(df_train) + len(df_test))
endLabel(start_time)

start_time             = startLabel('(9) Data Splitting - X and y - X_train and y_train')
X                      = df_train.copy()
y                      = X.pop('attendees') 
X_test                 = df_test.copy()
y_test                 = X_test.pop('attendees') 
endLabel(start_time)

start_time             = startLabel('(10) Data Splitting - Create Linear Regression Formula')
my_formula             = ' attendees ~ ' + '+'.join(df.columns[1:])
print('Formula:',my_formula)
endLabel(start_time)

start_time             = startLabel('(11) Fit Linear Regression Model')
est                    = ols(my_formula, data=df_train).fit()
print(est.summary())
endLabel(start_time)

start_time             = startLabel('(12) Define the OSR2 Helper function')
def OSR2(y_pred, y_true, training_mean):
  '''
  Calculates out-of-sample R-squared
  '''
  baseline_error       = np.sum(np.square((training_mean - y_true)))
  model_error          = np.sum(np.square((y_pred - y_true)))
  return 1.0 - model_error/baseline_error
endLabel(start_time)

start_time             = startLabel('(13) Calculate OSR2')
y_pred                 = est.predict(X_test)
osr2_result            = OSR2(y_pred, y_test, y.mean())
print('OSR2: ',osr2_result)
endLabel(start_time)

start_time             = startLabel('(14) Fit Decision Tree Regressor')
tree                   = DecisionTreeRegressor(max_depth=3, random_state=42)
print(tree)
endLabel(start_time)

start_time             = startLabel('(15) Fit Show X df Head')
print(X.head())
endLabel(start_time)

start_time             = startLabel('(16) One-Hot Encoding')
X                      = pd.get_dummies(X, columns = categoricals)
X_test                 = pd.get_dummies(X_test, columns = categoricals)
print('X shape     : ',X.shape)
print('X_test shape: ',X_test.shape)
endLabel(start_time)

start_time             = startLabel('(17) Show X.Head() after One-Hot Encoding')
print(X.head())
endLabel(start_time)

start_time             = startLabel('(18) Build a CART wih default parameters')
tree.fit(X,y)
print(tree)
endLabel(start_time)

start_time             = startLabel('(19) OSR2 for Decision Tree Regressor')
result                 = OSR2(tree.predict(X), y, y.mean())
print('OSR2 TRAIN:', result)
endLabel(start_time)

start_time             = startLabel('(20) Show how big the tree is')
tree_shape             = tree.tree_.node_count, tree.tree_.max_depth
print('Tree Shape (Node Count, Tree Depth): ',tree_shape)
endLabel(start_time)

start_time             = startLabel('(21) Show the Test OSR2 before pruning')
print('OSR2 TEST: ',OSR2(tree.predict(X_test), y_test, y.mean()))
endLabel(start_time)

start_time             = startLabel('(22) Create Tree after Pruning')
tree                   = DecisionTreeRegressor(random_state=42)
print(tree)
endLabel(start_time)

start_time             = startLabel('(23) Compute the cost-complexity pruning path')
path                   = tree.cost_complexity_pruning_path(X, y)
print('Path: ',path)
endLabel(start_time)

start_time             = startLabel('(24) Extracts and shows the cost-complexity pruning information')
ccp_alphas, impurities = path.ccp_alphas, path.impurities
alphas                 = ccp_alphas.tolist()
print('CCP Alphas: ',len(ccp_alphas))
print('Impurities: ',len(impurities))
print('Alphas    : ',len(alphas))
endLabel(start_time)

start_time             = startLabel('(25) Show the total number of alpha values')
print(f'Number of alpha values: {len(ccp_alphas)}')
endLabel(start_time)

start_time             = startLabel('(26) Generate about ~50 trees, evenly sampled from this group')
alphas_small           = ccp_alphas[::100]
alphas_small           = alphas_small[::-1]
print(f'Number of small alpha values created: {len(alphas_small)}')
endLabel(start_time)

start_time             = startLabel('(27) Train and evaluate multiple decision tree models')
r2_all = []
osr2_all = []
node_counts = []
for alpha in alphas_small:
    tree = DecisionTreeRegressor(random_state=42, ccp_alpha=alpha)
    tree.fit(X, y)
    y_pred = tree.predict(X_test)
    r2 = tree.score(X, y)
    osr2 = OSR2(y_pred, y_test, y.mean())
    r2_all.append(r2)
    osr2_all.append(osr2)
    node_counts.append(tree.tree_.__getstate__()['nodes'].shape[0])
print("R2 Quantity  : ",len(r2_all))
print("OSR2 Quantity: ",len(osr2_all))
endLabel(start_time)

start_time             = startLabel('(28) Extract the tree corresponding to the best OSR2')
opt_idx                = np.argmax(osr2_all)
print(f'Optimal index     : {opt_idx}')
print(f'Optimal alpha     : {alphas_small[opt_idx]}')
print(f'Optimal R^2       : {r2_all[opt_idx]}')
print(f'Optimal OSR^2     : {osr2_all[opt_idx]}')
print(f'Optimal node count: {node_counts[opt_idx]}')
endLabel(start_time)

start_time             = startLabel('(29) Trains a decision tree regressor using the optimal pruning parameter')
tree                   = DecisionTreeRegressor(random_state=42, ccp_alpha=alphas_small[opt_idx])
tree.fit(X,y)
print('Tree node count: ',tree.tree_.node_count)
print('Tree max depth : ',tree.tree_.max_depth)
endLabel(start_time)

start_time             = startLabel('(30) Show key parameters of the tree')
print('Tree node count    : ',tree.tree_.node_count)
print('Tree max depth     : ',tree.tree_.max_depth)
print('Tree ccp_alpha     : ',tree.ccp_alpha)
print('Tree impurity      : ',len(tree.tree_.impurity))
print('Tree children_left : ',len(tree.tree_.children_left))
print('Tree children_right: ',len(tree.tree_.children_right))
print('Tree feature       : ',len(tree.tree_.feature))
print('Tree threshold     : ',len(tree.tree_.threshold))
print('Tree value         : ',len(tree.tree_.value))
print('Tree value shape   : ',tree.tree_.value.shape)
endLabel(start_time)

start_time             = startLabel('(31) Creates a function to visualize a decision tree modele')
def viz_tree(tree, font=6, figsize=(300,150)):
  '''
  draws a classification tree
  '''
  plt.figure(figsize=figsize)  # set plot size (denoted in inches)
  _ = plot_tree(tree,
                feature_names=X.columns,
                filled=True,
                fontsize=font)
  plt.savefig('tree.png', dpi=300, bbox_inches='tight')
endLabel(start_time)

start_time             = startLabel('(32) Visualize the tree')
viz_tree(tree)
endLabel(start_time)

start_time = startLabel('(33) Show the test OSR2 after pruning')
osr2 = OSR2(tree.predict(X_test), y_test, y.mean())
print('OSR2: ',osr2)
endLabel(start_time)
print(Fore.MAGENTA + 100 * '-' + Fore.RESET)
print(Fore.MAGENTA + "-----------------------------------Total Elapsed Time --- %30.20f seconds ---" % (time.time() - all_time))
print(Fore.MAGENTA + 100 * '-' + Fore.RESET)