package lab3_1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class lab3_1 extends JFrame implements ActionListener {
    private JList<String> list;
    private JButton button;
    private JTextField textField;
    
    public lab3_1() {
        setTitle("Multiple Selection Example");
        setSize(300, 200);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        
        // Создание списка
        String[] items = new String[100];
        for (int i = 0; i < items.length; i++) {
			items[i] = "Item" + i;
		}
        
        list = new JList<>(items);
        list.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        
        // Создание кнопки
        button = new JButton("Выбрать");
        button.addActionListener(this);
        
        // Создание текстового поля
        textField = new JTextField();
        textField.setEditable(false);
        
        // Добавление компонентов на панель
        JPanel panel = new JPanel(new BorderLayout());
        panel.add(new JScrollPane(list), BorderLayout.CENTER);
        panel.add(button, BorderLayout.SOUTH);
        panel.add(textField, BorderLayout.NORTH);
        add(panel);
    }
    
    public void actionPerformed(ActionEvent e) {
        // Получение выбранных элементов
        Object[] selectedValues = list.getSelectedValues();
        StringBuilder sb = new StringBuilder();
        for (Object selectedValue : selectedValues) {
            sb.append(selectedValue.toString()).append(", ");
        }
        String selectedItems = sb.toString();
        
        // Удаление последней запятой и пробела
        if (selectedItems.length() > 0) {
            selectedItems = selectedItems.substring(0, selectedItems.length() - 2);
        }
        // Проверка суммарной длины строки
        if (selectedItems.length() > 100) {
            JOptionPane.showMessageDialog(this, selectedItems);
            return;
        }
        // Помещение выбранных элементов в текстовое поле
        textField.setText(selectedItems);
        
        
    }
    
    public static void main(String[] args) {
        lab3_1 frame = new lab3_1();
        frame.setVisible(true);
    }
}