package lab3_3;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class lab3_3 extends JFrame implements ActionListener {
    private JList<String> liftLeft;
    private JList<String> liftRight;
    private JButton button;
    private JTextField textField;
    private DefaultListModel<String> listModel;
    public lab3_3() {
        setTitle("Multiple Selection Example");
        setSize(200, 200);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        
        // Создание списков
        String[] items = new String[100];
        for (int i = 0; i < items.length; i++) {
			items[i] = "Item" + i;
		}
        
        liftLeft = new JList<String>(items);
        liftLeft.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        // Выходной список
        listModel = new DefaultListModel<String>();
        liftRight = new JList<String>(listModel);
        // Создание кнопки
        button = new JButton("Выбрать");
        button.addActionListener(this);
        
        // Создание текстового поля
        textField = new JTextField();
        textField.setEditable(false);
        
        // Добавление компонентов на панель
        JPanel panel = new JPanel(new BorderLayout());
        panel.add(new JScrollPane(liftLeft), BorderLayout.WEST);
        panel.add(new JScrollPane(liftRight), BorderLayout.CENTER);
        panel.add(button, BorderLayout.SOUTH);
        // panel.add(textField, BorderLayout.NORTH);
        add(panel);
    }
    
    public void actionPerformed(ActionEvent e) {
        // Получение выбранных элементов
        Object[] selectedValues = liftLeft.getSelectedValues();
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
        // Помещение выбранных элементов в другой список
        listModel.removeAllElements();
        listModel.addElement(selectedItems);
        
        
        
    }
    
    public static void main(String[] args) {
        lab3_3 frame = new lab3_3();
        frame.setVisible(true);
    }
}