import tkinter as tk
from tkinter import ttk

def min_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp, m, n

def calculate_distance():
    word1 = entry1.get()
    word2 = entry2.get()
    matrix, m, n = min_edit_distance(word1, word2)

    # Matris boyutunu kelimelerin uzunluğuna ayarla
    m = len(word1) + 1
    n = len(word2) + 1

    # Eğer matris boyutu değiştiyse, label listesini yeniden oluştur
    global matrix_labels
    for widget_list in matrix_labels:
        for widget in widget_list:
            widget.destroy()
    matrix_labels.clear()
    for i in range(m+1):
        row_labels = []
        for j in range(n+1):
            if i == 0 and j == 0:
                label_text = ""
            elif i == 0 and j == 1:
                label_text = ""
            elif i == 1 and j == 0:
                label_text = ""
            elif i == 0 and j > 1:
                label_text = word2[j-2]
            elif j == 0 and i > 1:
                label_text = word1[i - 2]
            else:
                label_text = str(matrix[i - 1][j - 1])

            fg_color = "lightgray" if i==j  else ("gray" if label_text == word1[i-2] or label_text==word2[j-2] else "white") # Kırmızı renk için koşul
            label = tk.Label(root, text=label_text, font=('calibri', 12), width=3, relief=tk.RIDGE, bg=fg_color )
            label.grid(row=i + 3, column=j + 2, padx=2, pady=2)
            row_labels.append(label)
        matrix_labels.append(row_labels)

root = tk.Tk()
root.title("Minimum Edit Distance Hesaplama")
root.geometry("900x700")

# Kelime girişleri için etiketler ve giriş alanları
label1 = tk.Label(root, text="Kelime 1:", font=('calibri', 14))
label1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry1 = tk.Entry(root, font=('calibri', 14))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Kelime 2:", font=('calibri', 14))
label2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry2 = tk.Entry(root, font=('calibri', 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

# Mesafe hesaplama düğmesi
calculate_button = ttk.Button(root, text="Mesafeyi Hesapla", command=calculate_distance, style='TButton')
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Mesafe matrisi için etiketler
matrix_labels = []
root.mainloop()
