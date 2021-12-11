{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a0619055-17a3-4125-8ae8-705a15ad9f75",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "screen=tk.Tk()\n",
    "screen.title(\"Matplot Graphies\")\n",
    "screen.geometry(\"500x500\")\n",
    "\n",
    "newlabel= tk.Label(text = \"cihan\")\n",
    "newlabel.grid(column=0,row=0)\n",
    "button_name = tk.Button(screen, text = \"some text\")\n",
    "button_name.grid(column=1,row=0)\n",
    "screen.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "7593e288-34e4-4f56-8460-d077b9766e80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                  Sum of Squares    df  Mean Squares        F\n",
      "--------------  ----------------  ----  ------------------  -----------------\n",
      "Between Groups           2739        3  913.0               6.708850424559112\n",
      "Wihtin Groups            1633.07    12  136.08888888888887\n",
      "Total                    4372.07    15\n",
      "None\n",
      "                  Sum of Squares    df  Mean Squares    F\n",
      "--------------  ----------------  ----  --------------  ---\n",
      "Between Groups                40     2  20.0            8.0\n",
      "Wihtin Groups                 30    12  2.5\n",
      "Total                         70    14\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import scipy.stats as ss\n",
    "from tabulate import tabulate\n",
    "#x=[[],[],[]]\n",
    "\n",
    "def one_way_anova(x):\n",
    "    N = []\n",
    "    k = len(x)\n",
    "    sums = []\n",
    "    sumsq = []\n",
    "    means = []\n",
    "    group_bwl = 0 #between\n",
    "    group_whl = 0 #within \n",
    "    if len(x)<3:\n",
    "        print(\"You must enter at least 3 groups!\")\n",
    "    else:\n",
    "        for i in range(k):\n",
    "            N.append(len(x[i]))\n",
    "            sums.append(np.sum(x[i])) \n",
    "            sumsq.append((np.sum(x[i]))**2)\n",
    "            means.append(np.mean(x[i]))\n",
    "            group_whl += np.var(x[i])*k\n",
    "        n = np.sum(N)\n",
    "    \n",
    "        totalmean = np.sum(sums) / n \n",
    "        \n",
    "            \n",
    "        for i in range(k):\n",
    "            group_bwl += N[i]*((means[i]-totalmean)**2)\n",
    "        \n",
    "        group_bw = group_bwl/(k-1)\n",
    "        group_wh = group_whl/(n-k)\n",
    "        \n",
    "        df1,df2 = k-1,n-k\n",
    "        F = group_bw / group_wh\n",
    "        t = [(group_bwl+group_whl),((k-1)+(n-k))]\n",
    "        \n",
    "        print(tabulate([['Between Groups', group_bwl,(k-1),group_bw,F], \n",
    "                        ['Wihtin Groups', group_whl,(n-k),group_wh,\"\"],\n",
    "                        ['Total',t[0],t[1],\"\",\"\"]],  \n",
    "                       headers=['','Sum of Squares', 'df','Mean Squares','F']))\n",
    "        \n",
    "#samples      \n",
    "b = [[5,7,8,6,4],[6,9,10,12,13],[7,8,9,10,6]]             \n",
    "a = [[47,32,63,54],[51,74,70],[68,46,49,53],[63,85,80,95,82]]\n",
    "print(one_way_anova(a))\n",
    "print(one_way_anova(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "f0a3fef0-4d1e-4a42-8d3d-7a0701b679cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Kareler Toplamı</th>\n",
       "      <th>Serbestlik Derecesi</th>\n",
       "      <th>Kareler Ortalaması</th>\n",
       "      <th>F hesap Oranı</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Gruplar Arası</th>\n",
       "      <td>606.75</td>\n",
       "      <td>3.0</td>\n",
       "      <td>202.25</td>\n",
       "      <td>1.479842</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gruplar İçi</th>\n",
       "      <td>1640.00</td>\n",
       "      <td>12.0</td>\n",
       "      <td>136.67</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Toplam</th>\n",
       "      <td>2246.75</td>\n",
       "      <td>15.0</td>\n",
       "      <td>-</td>\n",
       "      <td>-</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Kareler Toplamı  Serbestlik Derecesi Kareler Ortalaması  \\\n",
       "Gruplar Arası           606.75                  3.0             202.25   \n",
       "Gruplar İçi            1640.00                 12.0             136.67   \n",
       "Toplam                 2246.75                 15.0                  -   \n",
       "\n",
       "              F hesap Oranı  \n",
       "Gruplar Arası      1.479842  \n",
       "Gruplar İçi               -  \n",
       "Toplam                    -  "
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import scipy.stats as ss\n",
    "data = {\"Okul1\" : [47,32,63,54,np.nan],\n",
    "\"Okul2\" : [51,74,70,np.nan,np.nan],\n",
    "\"Okul3\" : [68,46,49,53,np.nan],\n",
    "\"Okul4\" : [63,85,80,95,82]}\n",
    "df = pd.DataFrame(data)\n",
    "N = [4,3,4,5]\n",
    "n = np.sum(N)\n",
    "toplamlar = df[[\"Okul1\",\"Okul2\",\"Okul3\",\"Okul4\"]].sum()\n",
    "ortalamalar = df[[\"Okul1\",\"Okul2\",\"Okul3\",\"Okul4\"]].mean()\n",
    "genelort = toplamlar.sum()/np.sum(N) # 63.25\n",
    "Gakt = 0\n",
    "for i in range(len(ortalamalar)):\n",
    "    Gakt += np.square(ortalamalar[i]-genelort)\n",
    "Gikt = (np.sum(np.square((df[\"Okul1\"]-df[\"Okul1\"].mean())))+\n",
    "         np.sum(np.square(df[\"Okul2\"]-df[\"Okul2\"].mean()))+\n",
    "          np.sum(np.square(df[\"Okul3\"]-df[\"Okul3\"].mean()))+\n",
    "           np.sum(np.square(df[\"Okul4\"]-df[\"Okul4\"].mean())))\n",
    "GKT = Gakt + Gikt\n",
    "tablo = pd.DataFrame(columns = [\"Kareler Toplamı\",\"Serbestlik Derecesi\",\"Kareler Ortalaması\",\"F hesap Oranı\"],\n",
    "                    index=[\"Gruplar Arası\",\"Gruplar İçi\"])\n",
    "k = len(df.columns)\n",
    "tablo[\"Kareler Toplamı\"] = [Gakt,Gikt]\n",
    "tablo[\"Serbestlik Derecesi\"] = [k-1,n-k]\n",
    "tablo[\"Kareler Ortalaması\"] = np.round([Gakt/(k-1),Gikt/(n-k)],2)\n",
    "tablo[\"F hesap Oranı\"] = tablo[\"Kareler Ortalaması\"][0]/tablo[\"Kareler Ortalaması\"][1]\n",
    "tablo.loc[\"Toplam\"] = tablo.sum()\n",
    "tablo.iloc[1,3],tablo.iloc[2,2],tablo.iloc[2,3] = [\"-\",\"-\",\"-\"]\n",
    "tablo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "b54120cb-ba37-40fd-a1da-32f9533fe305",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10.0"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
