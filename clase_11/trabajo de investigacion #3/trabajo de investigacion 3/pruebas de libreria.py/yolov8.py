import sys

try:
    from ultralytics import YOLO
except ImportError:
    print("[ERROR] La librería 'ultralytics' no está instalada.")
    print("Ejecuta en tu terminal: pip install ultralytics")
    sys.exit(1)


def demo_yolov8():
    # 1. Cargar el modelo YOLOv8 Small preentrenado en COCO dataset
    model = YOLO("yolov8s.pt")

    # 2. Imprimir información de la arquitectura (capas, parámetros, FLOPs)
    print("\n--- Información del Modelo ---")
    model.info()

    # 3. Realizar la inferencia sobre una imagen
    source_img = "https://ultralytics.com/images/bus.jpg"

    print("\n--- Ejecutando Inferencia ---")
    results = model.predict(source=source_img, conf=0.25, save=True)

    # 4. Procesar y mostrar los resultados obtenidos
    for result in results:
        boxes = result.boxes
        print(f"\n[ÉXITO] Se detectaron {len(boxes)} objetos en la imagen.")
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls_id]
            print(f" -> Clase: {name} | Confianza: {conf:.2%}")


if __name__ == "__main__":
    demo_yolov8()
