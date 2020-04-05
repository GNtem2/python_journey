# python_journey
learning python
These codes are part of my journey learning python. 

Machine learning-Random Forest:
This part focusses on machine learning and use sklearn. Random forest is , a supervised machine learning method related to decision tree analysis, which employed random selection of covariates and patients from the dataset to create multiple trees. This form of ensemble learning utilises ‘wisdom of the crowd’ to create the model. This example illustrates the use of regression with random forest and a plot of observed vs predicted is provided in RFstandfirm.ipynb notebook. An example with random forest classification is provided in the DrivingReg.ipynb notebook. This example comes with demo of creation of GUI for testing new data using the model created by random forest. 

[![here](./RFstandfirm_regression.png)](./RFstandfirm.ipynb)

Machine learning-TSNE:
This part focusses on manifold learning and uses sklearn manifold tsne. The T-distributed Stochastic Neighbor Embedding example is provided below. This is a low dimensional representation of the thrombectomy trial data. 

Handling dataframe:
The file also contains illustration about opening of R files in the form of .Rda. You will need to import pyreadr and pyreadr.read_r("name of file.rda"). Xcel files like csv can be opened using pandas. You will need to import pandas as pd then run this line pd.read_csv("name of file.csv"). 

```python
import pandas as pd
import pyreadr 
pd.read_csv('name of file.csv')
```
Pandas data frame can be merged using pd.concat([file1,file2],axis=1). The line axis=1 indicates that the merge is by columns. Similarly, dropping a column is performed by specifying drop after name of file such as file.drop (['name of column'],axis=1). Selecting a column from data frame can be done by writing file['name of column']. selcting multiple columns require [['name of column1','name of column2']].

Conversion from wide to long format:
For the time being the conversion from wide to long format is done in R. see the datawrangling.R file.

Plotting:
There are illustrations with 3 types of plot: seaborn, matplotlib and plotnine-ggplot style.

The seaborn plot is shown. 
```python
import seaborn as sns
#tsne_df is a data frame with columns X, Y, Disability
sns.scatterplot(x="X", y="Y",
              hue="Positive",
              palette=['blue','red'],
              legend='full',
              data=tsne_df);
```
[![here](./TSNEecr_sns.png)](./TSNEecr.ipynb)

The matplotlib plot is shown.
```python
import matplotlib as plt
fig, ax = plt.subplots()
ax.scatter(tsne_obj [:,0], tsne_obj[:,1], c=y)
ax.set_xlabel('tsne_obj [:,0] ')
ax.set_ylabel('tsne_obj [:,1] ')
ax.set_title("TSNE")
plt.show() #plt calls the matplotlib
```
![here](./TSNEecr_matplotlib.png)

The plotnine plot is shown. This is a ggplot style in python.
```python
from plotnine import *  
(ggplot (df)
 + geom_point(aes('X ', 'Y',color='factor(Disability)',shape='factor(Akmed)'))
)+labs(color="Disability",shape='Trajectory')
```
![here](./TSNEecr_plotnine.png)

Geospatial analysis:
This part focusses on geospatial analysis and use the osmnx library. The tutorial paper is available [here](https://www.frontiersin.org/articles/10.3389/fneur.2019.00743/full). This section was done by setting up an environment for geospatial analysis using Miniconda

The  python notebook deals with journey from Westin Hotel to surrounding building within 500 metres radius. 

```python
#see the code in Brisbane.ipynb notebook
origin=ox.utils.geocode('147 Charlotte St, Brisbane, Queensland') #Queensland Health
origin_node=ox.get_nearest_node(G,origin)
destination= ox.utils.geocode('The Westin Hotel, Brisbane, Queensland')
destination_node=ox.get_nearest_node(G,destination)
route = nx.shortest_path(G, origin_node, destination_node)
ox.plot_graph_route(G, route)
```
[![Brisbane.ipynb](./Westin.png](./Brisbane.ipynb)

A second example uses codes provided from osmnx for examining street network orientation in Australian Capital Cities. The AustCities-Copy1.ipynb note book is available in gh-pages.  The codes have been adapted from Geof Boeing's OSMNX page. 

[![here](./AustCities.png)](./AustCities-Copy1.ipynb).
