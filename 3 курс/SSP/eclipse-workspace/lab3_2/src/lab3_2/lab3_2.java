package lab3_2;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

public class lab3_2 extends JFrame {
    private JList<String> itemList;
    private DefaultListModel<String> listModel;
    //private JTextField textField;
    private JCheckBox oddCheckBox;
    private JCheckBox evenCheckBox;
    private JComboBox<String> comboBox;

    public lab3_2() {
        setTitle("List Management App");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        // Создание списка и модели данных
        listModel = new DefaultListModel<>();
        for (int i = 0; i < 10; i++) {
                listModel.addElement("Item " + i);
        }
        itemList = new JList<>(listModel);
        itemList.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        JScrollPane scrollPane = new JScrollPane(itemList);
        scrollPane.setPreferredSize(new Dimension(200, 150));
        add(scrollPane);

        // Создание текстового поля
       // textField = new JTextField(20);
       // add(textField);

        // Создание флажков
        oddCheckBox = new JCheckBox("Выбрать нечетные строки");
        evenCheckBox = new JCheckBox("Выбрать четные строки");
        add(oddCheckBox);
        add(evenCheckBox);

        // Создание раскрывающегося списка
        comboBox = new JComboBox<>();
        comboBox.setPreferredSize(new Dimension(200, 150));
        add(comboBox);

        // Обработка событий флажков
        ItemListener checkBoxListener = new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getSource() == oddCheckBox) {
                    if (oddCheckBox.isSelected()) {
                        selectOddItems();
                    } else {
                        deselectOddItems();
                    }
                } else if (e.getSource() == evenCheckBox) {
                    if (evenCheckBox.isSelected()) {
                        selectEvenItems();
                    } else {
                        deselectEvenItems();
                    }
                }
            }
        };
        oddCheckBox.addItemListener(checkBoxListener);
        evenCheckBox.addItemListener(checkBoxListener);

        pack();
        setVisible(true);
    }

    private void selectOddItems() {
         for (int i = 0; i < 10; i++) {
             if (i % 2 != 0) {
            	 itemList.addSelectionInterval(i, i);
                 comboBox.addItem("Item " + i);
             }
         }
    }

    private void deselectOddItems() {
        for (int i = 1; i < 10; i+=2) {
       	 	itemList.removeSelectionInterval(i, i);
       	 	comboBox.removeItem("Item "+i);
        }
    }

    private void selectEvenItems() {
        for (int i = 0; i < 10; i+=2) {
            	itemList.addSelectionInterval(i, i);
                comboBox.addItem("Item " + i);
        }
    }

    private void deselectEvenItems() {
        for (int i = 0; i < 10; i+=2) {
       	 	itemList.removeSelectionInterval(i, i);
       	 	comboBox.removeItem("Item "+i);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new lab3_2();
            }
        });
    }
}